{
  description = "Svelte-powered site";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    flake-utils.inputs.nixpkgs.follows = "nixpkgs";
    bp.url = "github:serokell/nix-npm-buildpackage";
    bp.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = { self, nixpkgs, flake-utils, bp, ... }:
    (flake-utils.lib.eachDefaultSystem
      (system:
        let
          pkgs = import nixpkgs { inherit system; };
          node = pkgs.nodejs-18_x;
          yarn18 = pkgs.yarn.overrideAttrs (old: { buildInputs = [ node ]; });
          python-deps = with pkgs.python310Packages; [
            python-telegram-bot
            sqlalchemy
          ];
          python-dev-deps = with pkgs.python310Packages; [
            mypy
            black
            isort
          ];
          website = bp.legacyPackages.x86_64-linux.buildYarnPackage {
            src = ./website;
            installPhase = ''
              yarn build
              rm -rf node_modules/
              cat <<-END >> .yarnrc
                yarn-offline-mirror "$PWD/yarn-cache"
                nodedir "${node}"
              END
              yarn install --production --cache-folder "$PWD/yarn-cache" || true
              cp -r build $out/
              cp -r node_modules $out/
              cp package.json $out/
              cp yarn.lock $out/
              mkdir $out/bin
              cat <<EOF > $out/bin/archive-bot
                #!${pkgs.bash}/bin/bash
                ${node}/bin/node $out/index.js
              EOF
              chmod u+x $out/bin/archive-bot
            '';
          };
          bot = pkgs.python310Packages.buildPythonPackage rec {
            name = "archive-bot";
            src = ./bot;
            propagatedBuildInputs = python-deps;
          };
        in
        {
          devShells.default = pkgs.mkShell {
            buildInputs = (with pkgs; [
              node
              yarn18
            ]) ++ python-deps ++ python-dev-deps;
          };

          packages.website = website;
          packages.bot = bot;
        }
      )) // {
      nixosModules.default = ({ config, lib, pkgs, ... }:
        with lib; let
          cfg = config.services.archive-bot;
        in
        {
          options.services.archive-bot = {
            enable = mkEnableOption "Enable archive bot";

            host = mkOption {
              type = types.str;
              default = "0.0.0.0";
              description = "Address to listen";
            };

            port = mkOption {
              type = types.port;
              default = 3000;
              description = "Port to listen";
            };

            domain = mkOption {
              type = types.str;
              description = "Domain to use";
            };

            environment = mkOption {
              type = types.path;
              description = "Path to bot environment with secrets";
            };

            workdir = mkOption {
              type = types.path;
              default = "/var/lib/archive-bot";
              description = "Working directory for archive bot";
            };

            website-package = mkOption {
              type = types.package;
              default = self.packages.x86_64-linux.website;
              description = "What website package to use";
            };

            bot-package = mkOption {
              type = types.package;
              default = self.packages.x86_64-linux.bot;
              description = "What bot package to use";
            };
          };

          config.systemd.services = mkIf cfg.enable {
            archive-bot-website = {
              enable = true;
              description = "archive bot website";
              script = "${cfg.website-package}/bin/archive-bot";
              environment = {
                HOST = cfg.host;
                PORT = builtins.toString cfg.port;
              };
              unitConfig = {
                Type = "simple";
              };
              serviceConfig = {
                User = "archive-bot";
                Group = "archive-bot";
                Restart = "on-failure";
                RestartSec = "1s";
              };
              wantedBy = [ "multi-user.target" ];
            };

            archive-bot = {
              enable = true;
              description = "archive bot";
              script = "${cfg.bot-package}/bin/archive-bot";
              requires = [ "archive-bot-website.service" ];
              environment = {
                DOMAIN = cfg.domain;
              };
              unitConfig = {
                Type = "simple";
              };
              serviceConfig = {
                User = "archive-bot";
                Group = "archive-bot";
                Restart = "on-failure";
                RestartSec = "1s";
                Environment = cfg.bot-environment;
                WorkingDirectory = cfg.workdir;
              };
              wantedBy = [ "multi-user.target" ];
            };
          };

          config.users = mkIf cfg.enable {
            users.archive-bot = {
              isSystemUser = true;
              description = "archive bot user";
              group = "archive-bot";
              home = cfg.workdir;
              createHome = true;
            };

            groups.archive-bot = { };
          };
        });
    };
}
