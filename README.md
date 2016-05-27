# Ansible

Master: [![Build Status](https://travis-ci.org/sansible/ansible.svg?branch=master)](https://travis-ci.org/sansible/ansible)  
Develop: [![Build Status](https://travis-ci.org/sansible/ansible.svg?branch=develop)](https://travis-ci.org/sansible/ansible)

* [ansible.cfg](#ansible-cfg)
* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This roles installs Ansible.




## ansible.cfg

This role is designed to work with merge "hash_behaviour". Make sure your
ansible.cfg contains these settings

```INI
[defaults]
hash_behaviour = merge
```




## Installation and Dependencies

To install run `ansible-galaxy install sansible.ansible` or add this to your
`roles.yml`.

```YAML
- name: sansible.ansible
  version: v1.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`




## Tags

This role uses one tag: **build**

* `build` - Installs Ansible and all it's dependencies.




## Examples

To install:

```YAML
- name: Install and configure Ansible
  hosts: "somehost"

  roles:
    - role: sansible.ansible
```

With version specified:

```YAML
- name: Install and configure Ansible
  hosts: "somehost"

  roles:
    - role: sansible.ansible
      ansible:
        version: 1.9.6
```
