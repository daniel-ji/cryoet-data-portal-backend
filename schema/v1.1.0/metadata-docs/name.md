

# Slot: name

URI: [cdp-meta:name](metadataname)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AuthorMixin](AuthorMixin.md) | An entity with author data |  no  |
| [Author](Author.md) | Author of a scientific data entity |  no  |
| [CellType](CellType.md) | The cell type from which the sample was derived |  no  |
| [CellComponent](CellComponent.md) | The cellular component from which the sample was derived |  no  |
| [AnnotationObject](AnnotationObject.md) | Metadata describing the object being annotated |  no  |
| [AnnotationMethodLinks](AnnotationMethodLinks.md) | A set of links to models, sourcecode, documentation, etc referenced by annota... |  no  |
| [CellStrain](CellStrain.md) | The strain or cell line from which the sample was derived |  no  |
| [TissueDetails](TissueDetails.md) | The type of tissue from which the sample was derived |  no  |
| [OrganismDetails](OrganismDetails.md) | The species from which the sample was derived |  no  |







## Properties

* Range: [Any](Any.md)





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cdp-meta:name |
| native | cdp-meta:name |




## LinkML Source

<details>
```yaml
name: name
alias: name
domain_of:
- Author
- OrganismDetails
- TissueDetails
- CellType
- CellStrain
- CellComponent
- AnnotationObject
- AuthorMixin
- AnnotationMethodLinks
range: Any

```
</details>
