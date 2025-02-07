{
  "targets": [
    {
      "target_name": "kpathsea",
      "sources": [
        "src/kpathsea.cc",
      ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "/opt/homebrew/opt/texlive/include/"
      ],
      "link_settings": {
        "libraries": [
          "-L/opt/homebrew/opt/texlive/lib/",
          "-lkpathsea"
        ],
      },
    },
  ],
}
