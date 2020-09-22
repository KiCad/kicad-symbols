## :warning: Deprecation warning
In preparation for the KiCad v6 release this repository will be locked down on Sept 1, 2020. No new pull requests will be accepted. Existing pull requests can be worked on until Oct 1, 2020. Changes breaking v5.1 compatibility can be merged starting Sept 1, 2020.

On Oct 1, 2020 this repository, including issues and pull requests, will be archived and transferred to [gitlab.com](https://gitlab.com/kicad/libraries/kicad-symbols/). In order for your pull requests and issues to be imported into GitLab you must set your email address on GitHub to public and use the same address for your GitLab account. Or login to GitLab at least once using the GitHub icon. Otherwise the importer can't correlate the account information and the issues/comments on GitLab will be owned by `kicad-bot` ([importer documentation](https://docs.gitlab.com/ee/user/project/import/github.html#how-it-works)).

We plan to convert the library to the new v6 S-expr format after it is imported to GitLab. That also means that old pull requests will need to be redone with the v6 format if they are not merged before then.

# KiCad Symbols

This repository contains the official KiCad schematic symbol libraries.

**The libraries in this repositiory are intended for KiCad version 5.x**

Each symbol library is stored as a `.lib` and `.dcm` file pair.

Weekly builds can be found at https://kicad.github.io/symbols

Contribution guidelines can be found at http://kicad-pcb.org/libraries/contribute
The library convention can be found at http://kicad-pcb.org/libraries/klc/

Other KiCad library repositories are located:

* Footprints: https://github.com/kicad/kicad-footprints
* 3D Models: https://github.com/kicad/kicad-packages3d
* Templates: https://github.com/kicad/kicad-templates
