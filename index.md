---
title: Registry metadata
---
All the [IATI registry](https://iatiregistry.org) metadata, in two files.

<div class="row">
  {% include card.html fname="publisher_list.json" title="all publishers metadata" description="A list of publisher metadata from the registry" %}

  {% include card.html fname="dataset_list.json" title="all datasets metadata" description="A list of dataset metadata from the registry" %}
</div>

{% assign now = site.time | date_to_rfc822 %}

_Both files update every 3-4 hours. Last updated: <abbr title="{{ now }}" id="last-updated">{{ now }}</abbr>._

---

**_\*BONUS!\*_** A CSV of [mappings of past to current publisher IDs](registry_id_relationships.csv)
