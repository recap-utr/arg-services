{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    systems.url = "github:nix-systems/default";
  };
  outputs =
    inputs@{
      flake-parts,
      systems,
      ...
    }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = import systems;
      perSystem =
        { pkgs, ... }:
        let
          packages = [ pkgs.buf ];
        in
        {
          packages.release-env = pkgs.buildEnv {
            name = "release-env";
            paths = packages;
          };
          devShells.default = pkgs.mkShell {
            inherit packages;
          };
        };
    };
}
