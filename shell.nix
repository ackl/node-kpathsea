{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    # nativeBuildInputs is usually what you want -- tools you need to run
    nativeBuildInputs = [
      pkgs.nodePackages.node-gyp
      pkgs.python3
    ];
    LDFLAGS="-L${pkgs.texlive.bin.core}/lib";
    CXXFLAGS="-I${pkgs.texlive.bin.core.dev}/include";
  }
 

