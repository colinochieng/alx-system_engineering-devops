#  Configuration management
## Resources
### Read or watch:
- [Intro to Configuration Managemen](https://intranet.alxswe.com/rltoken/GL30hu-aRcKzPOvK8JO-Bg)
- [Puppet resource type: file (check “Resource types” for all manifest types in the left menu)](https://intranet.alxswe.com/rltoken/WON0M4DNRabf88KAG_pDUA)
- [Puppet’s Declarative Language: Modeling Instead of Scripting](https://intranet.alxswe.com/rltoken/0V2fBdafkfKPMxA1umea3Q)
- [Puppet lint](https://intranet.alxswe.com/rltoken/CRUMeEMdcX-UtbWsUM9xLQ)
- [Puppet emacs mode](https://intranet.alxswe.com/rltoken/MzHXCntAkPzOqMnI6_rpWQ)

## Requirements
### General
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension .pp

## Note on Versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```
You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

[Puppet 5 Docs](https://intranet.alxswe.com/rltoken/fsIr2xFkJHTkaXwqZFFcbA)

# Install `puppet-lint`

```$ gem install puppet-lint```