# Slot: energy_filter


_Energy filter setup used_



URI: [cdp-meta:energy_filter](metadataenergy_filter)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MicroscopeOpticalSetup](MicroscopeOpticalSetup.md) | The optical setup of the microscope used to collect the tilt series |  no  |







## Properties

* Range: [xsd:string](http://www.w3.org/2001/XMLSchema#string)





## Identifier and Mapping Information







### Schema Source


* from schema: metadata




## LinkML Source

<details>
```yaml
name: energy_filter
description: Energy filter setup used
from_schema: metadata
exact_mappings:
- cdp-common:tiltseries_microscope_energy_filter
rank: 1000
alias: energy_filter
owner: MicroscopeOpticalSetup
domain_of:
- MicroscopeOpticalSetup
range: string
inlined: true
inlined_as_list: true

```
</details>
