module.exports = {
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
          "mkdir -p images",
          "buf build -o images/arg-services.binpb",
          "buf build images/arg-services.binpb -o images/arg-services.txtpb",
          "buf build images/arg-services.binpb -o images/arg-services.json",
        ].join(" && "),
        // labels the commit with the release tag
        publishCmd: "buf push --git-metadata",
      },
    ],
    [
      "@semantic-release/github",
      {
        assets: ["images/*"],
        failComment: false,
        successComment: false,
        addReleases: "bottom",
      },
    ],
    [
      "@semantic-release/git",
      {
        message: "chore(release): ${nextRelease.version}",
        assets: ["CHANGELOG.md"],
      },
    ],
  ],
};
