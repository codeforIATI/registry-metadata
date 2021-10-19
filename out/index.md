---
title: Registry metadata
---
All the [IATI registry](https://iatiregistry.org) metadata, in two files.

<div class="row">
  {% include card.html fname="/publisher_list.json" title="All publishers metadata" description="A list of publisher metadata from the registry" %}

  {% include card.html fname="/dataset_list.json" title="All datasets metadata" description="A list of dataset metadata from the registry" %}
</div>

{% assign now = site.time | date_to_rfc822 %}

_Both files last updated: <abbr title="{{ now }}" id="last-updated">{{ now }}</abbr>._
