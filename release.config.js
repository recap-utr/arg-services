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
      "@semantic-release/exec",
      {
        prepareCmd: [
          // Buf
          "buf generate",
          "cp README.md buf.md",
          "find ./src/python ./src/typescript ./src/java -type d -maxdepth 0 -exec cp README.md {} ;",
          // Python
          "cd src/python",
          "poetry version ${nextRelease.version}",
          "find ./arg_services -type d -exec touch {}/__init__.py \\;",
          "cd -",
        ].join(" && "),
        publishCmd: [
          // Buf
          "buf push --tag ${nextRelease.version}",
          // Python
          "cd src/python",
          "poetry publish --build --username __token__ --password $PYPI_TOKEN --no-interaction -vvv",
          "cd -",
        ].join(" && "),
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
      "@semantic-release/github",
      {
        assets: [
          { path: "src/python/dist/*.tar.gz", label: "python-sdist" },
          { path: "src/python/dist/*.whl", label: "python-wheel" },
          { path: "src/python/dist/*.tgz", label: "npm" },
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
