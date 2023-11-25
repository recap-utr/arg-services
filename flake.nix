{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    systems.url = "github:nix-systems/default";
  };
  outputs = inputs @ {
    nixpkgs,
    flake-parts,
    systems,
    ...
  }:
    flake-parts.lib.mkFlake {inherit inputs;} {
      systems = import systems;
      perSystem = {
        pkgs,
        system,
        lib,
        self',
        ...
      }: {
        packages = {
          releaseEnv = pkgs.buildEnv {
            name = "release-env";
            paths = with pkgs; [buf];
          };
        };
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [buf];
        };
      };
    };
}
