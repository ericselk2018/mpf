# PyInstaller Temporary Notes

I run this command inside the mpf folder (where `__main__.py` is located):

```
pyinstaller __main__.py --noconfirm --clean --add-data="config_spec.yaml;./mpf/" --add-data="mpfconfig.yaml;./mpf/" --add-data="./modes/attract/config/attract.yaml;./mpf/modes/attract/config/" --add-data="./modes/game/config/game.yaml;./mpf/modes/game/config/" --onefile
```

The above command should create some files in /mpf/dist/ folder. You should be able to copy main.exe to mc_demo machine folder and run it with different command-line options that "game" supports (not MC options). This works for me on two different Windows 10 PCs, including one with nothing Python or MPF installed. I have only tested with these exact command-line options, other options will likely try to load other dynamic imports and fail to run unless they are also added to the package, same with trying to run from a machine other than mc_demo: `-XbvV`

Replace `--onefile` with `--debug=noarchive` to see what all is packaged inside the EXE, this mode will put all of the files in the subfolder instead of inside the EXE so you can easily see what is in the EXE (the EXE self extracts to a temp folder on each run). `--debug=imports` and `--debug=all` are also helpful at times.

# Mission Pinball Framework (MPF)

<img align="center" height="146" src="https://missionpinball.org/images/mpf-logo-full.png"/>

<em>...Let's build a pinball machine!</em>

## What is Mission Pinball Framework?

Mission Pinball Framework (MPF) is open source, cross-platform software for powering real pinball
machines. MPF is a community-developed project released under the MIT license. It's supported by volunteers in their spare time.

[![Coverage Status](https://coveralls.io/repos/missionpinball/mpf/badge.svg?branch=dev&service=github)](https://coveralls.io/github/missionpinball/mpf?branch=dev)
[![Test Status](https://github.com/missionpinball/mpf/actions/workflows/run_tests.yml/badge.svg)](https://github.com/missionpinball/mpf/actions/workflows/run_tests.yml)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/1687/badge)](https://bestpractices.coreinfrastructure.org/projects/1687)

Visit the MPF project homepage at https://missionpinball.org. Additional related projects exist as part of the MPF ecosystem, including the "MPF Monitor" which is a graphical application that lets you simulate pinball hardware, and "MPF-MC" which is a media controller which provides graphics and sounds for pinball machines.

## Documentation

-   User Docs (installation, tutorials, & reference): https://docs.missionpinball.org
-   Developer documentation: https://developer.missionpinball.org/

## Support

MPF is an open source community project which has no official support. Some MPF users participate in the MPF-Users Google group: https://groups.google.com/forum/#!forum/mpf-users.

Individual pinball hardware companies may provide additional support for users of their hardware, often via their own Slack, Discord, or other chat groups. If you get stuck, you can ask for help in the MPF-users group, or you reach out to your hardware provider.

## Maintenance, Pull Requests, & Bug Fixes

As a community project, we welcome pull requests and bug fixes. However, we do not have the resources to provide support for MPF. If you are interested in becoming a maintainer, please contact us at brian@missionpinball.org.

Bugs or other issues related to MPF itself can be posted to the [MPF Discussions page on GitHub](https://github.com/orgs/missionpinball/discussions).

## Contributing

Individual pinball hardware makers are responsible for their own platform interface maintenance and contributions.

If you're a Python coder, documentation writer, or pinball maker, feel free to make a change and submit a pull request. For more information about contributing see the [Contributing Code](http://docs.missionpinball.org/about/contributing_to_mpf.html)
and [Contributing Documentation](http://docs.missionpinball.org/about/contributing_to_mpf_docs.html) pages.

## License

MPF and related projects are released under the MIT License. Refer to the LICENSE file for details. Docs are released under Creative Commons CC BY 4.0.
