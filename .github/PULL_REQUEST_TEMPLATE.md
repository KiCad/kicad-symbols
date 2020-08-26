*Replace this line with your commit message! Please provide a description of your pull request*

---

## :warning: Deprecation warning
In preparation for the KiCad v6 release this repository will be locked down on Sept 1, 2020. No new pull requests will be accepted. Existing pull requests can be worked on until Oct 1, 2020. Changes breaking v5.1 compatibility can be merged starting Sept 1, 2020.

On Oct 1, 2020 this repository, including issues and pull requests, will be archived and transferred to [gitlab.com](https://gitlab.com/kicad/libraries/kicad-symbols/). In order for your pull requests and issues to be imported into GitLab you must set your email address on GitHub to public and use the same address for your GitLab account. Or login to GitLab at least once using the GitHub icon. Otherwise the importer can't correlate the account information and the issues/comments on GitLab will be owned by `kicad-bot` ([importer documentation](https://docs.gitlab.com/ee/user/project/import/github.html#how-it-works)).

We plan to convert the library to the new v6 S-expr format after it is imported to GitLab. That also means that old pull requests will need to be redone with the v6 format if they are not merged before then.

---

All contributions to the kicad library must follow the [KiCad library convention](http://kicad-pcb.org/libraries/klc/)

Thanks for creating a pull request to contribute to the KiCad libraries! To speed up integration of your PR, please check the following items:

- [ ] Provide a URL to a datasheet for the symbol(s) you are contributing
- [ ] Provide a screenshot of the symbol(s) from the symbol editor with the pin types visible
- [ ] Ensure that the associated footprints match the [official footprint library](https://github.com/kicad/kicad-footprints)
  - A new fitting footprint must be submitted if the library does not yet contain one.
- [ ] If there are matching footprint PRs, provide link(s) as appropriate
- [ ] Check the output of the Travis automated check scripts - fix any errors as required
- [ ] Give a reason behind any intentional library convention rule violation.

---

Be patient, we maintainers are volunteers with limited time and need to check your contribution against the datasheet. You can speed up the process by providing all the necessary information (see above). And you can speed up the process even more by providing additional info like the screenshot of the symbol editor pin table (or for high pin counts converted to csv) sorted in the same way as the pin table in the datasheet and a direct link to the datasheet page that contains the pin table.
