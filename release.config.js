const config = {
  branches: [
    { name: "main" },
    { name: "next" },
    { name: "+([0-9])?(.{+([0-9]),x}).x" },
    { name: "dev", prerelease: true },
    { name: "beta", prerelease: true },
    { name: "alpha", prerelease: true },
  ],
  plugins: [
    [
      "@semantic-release/commit-analyzer",
      {
        preset: "conventionalcommits",
      },
    ],
    [
      "@semantic-release/release-notes-generator",
      {
        preset: "conventionalcommits",
      },
    ],
    [
      "@semantic-release/changelog",
      {
        changelogTitle: "# Changelog",
      },
    ],
    [
      // Buf
      "@semantic-release/exec",
      {
        prepareCmd: [
          // These are added to the release workflow in an attempt to mitigate rate limits by GitHub
          // "buf lint",
          // "buf breaking --against 'https://github.com/recap-utr/arg-services.git#branch=main,ref=HEAD~1'",
          "buf mod update",
          "cp README.md buf.md",
        ].join(" && "),
        publishCmd: "buf push --tag v${nextRelease.version}",
      },
    ],
    "@semantic-release/github",
    [
      "@semantic-release/git",
      {
        assets: ["CHANGELOG.md", "buf.lock"],
      },
    ],
  ],
};

module.exports = config;
