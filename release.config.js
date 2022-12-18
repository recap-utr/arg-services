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
          "buf generate",
          "cp README.md buf.md",
          "find ./src/python ./src/typescript ./src/java -type d -maxdepth 0 -exec cp README.md {} \\;",
        ].join(" && "),
        publishCmd: "buf push --tag ${nextRelease.version}",
      },
    ],
    [
      // Python
      "@semantic-release/exec",
      {
        execCwd: "src/python",
        prepareCmd:
          "find ./arg_services -type d -exec touch {}/__init__.py \\;",
      },
    ],
    [
      "@semantic-release/npm",
      {
        pkgRoot: "src/typescript",
        tarballDir: "dist",
      },
    ],
    [
      "@cihelper/semanticrelease-plugin-poetry",
      {
        pkgRoot: "src/python",
      },
    ],
    [
      "@semantic-release/github",
      {
        assets: [
          { path: "src/python/dist/*.tar.gz", label: "python-sdist" },
          { path: "src/python/dist/*.whl", label: "python-wheel" },
          { path: "src/typescript/dist/*.tgz", label: "npm" },
        ],
      },
    ],
    [
      "@semantic-release/git",
      {
        assets: [
          "CHANGELOG.md",
          // Python
          "src/python/pyproject.toml",
          // TypeScript
          "src/typescript/package.json",
          "src/typescript/package-lock.json",
        ],
      },
    ],
  ],
};

module.exports = config;
