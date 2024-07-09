

# Class: AnnotationSemanticSegmentationMaskFile


_File and sourcing data for a semantic segmentation mask annotation. Annotation that identifies classes of objects._





URI: [cdp-meta:AnnotationSemanticSegmentationMaskFile](metadataAnnotationSemanticSegmentationMaskFile)






```mermaid
 classDiagram
    class AnnotationSemanticSegmentationMaskFile
    click AnnotationSemanticSegmentationMaskFile href "../AnnotationSemanticSegmentationMaskFile"
      AnnotationSourceFile <|-- AnnotationSemanticSegmentationMaskFile
        click AnnotationSourceFile href "../AnnotationSourceFile"
      
      AnnotationSemanticSegmentationMaskFile : file_format
        
      AnnotationSemanticSegmentationMaskFile : glob_string
        
      AnnotationSemanticSegmentationMaskFile : is_visualization_default
        
      AnnotationSemanticSegmentationMaskFile : mask_label
        
      
```





## Inheritance
* [AnnotationSourceFile](AnnotationSourceFile.md)
    * **AnnotationSemanticSegmentationMaskFile**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [mask_label](mask_label.md) | 0..1 <br/> [Integer](Integer.md) | The mask label for a semantic segmentation mask annotation file | direct |
| [file_format](file_format.md) | 0..1 <br/> [String](String.md) |  | direct |
| [glob_string](glob_string.md) | 0..1 <br/> [String](String.md) |  | direct |
| [is_visualization_default](is_visualization_default.md) | 0..1 <br/> [String](String.md) |  | direct |







## Aliases


* SemanticSegmentationMask



## Identifier and Mapping Information







### Schema Source


* from schema: metadata




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cdp-meta:AnnotationSemanticSegmentationMaskFile |
| native | cdp-meta:AnnotationSemanticSegmentationMaskFile |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnnotationSemanticSegmentationMaskFile
description: File and sourcing data for a semantic segmentation mask annotation. Annotation
  that identifies classes of objects.
from_schema: metadata
aliases:
- SemanticSegmentationMask
is_a: AnnotationSourceFile
attributes:
  mask_label:
    name: mask_label
    description: The mask label for a semantic segmentation mask annotation file.
    from_schema: metadata
    exact_mappings:
    - cdp-common:annotation_source_file_mask_label
    rank: 1000
    ifabsent: int(1)
    alias: mask_label
    owner: AnnotationSemanticSegmentationMaskFile
    domain_of:
    - AnnotationSemanticSegmentationMaskFile
    range: integer
    inlined: true
    inlined_as_list: true
  file_format:
    name: file_format
    from_schema: metadata
    exact_mappings:
    - cdp-common:annotation_source_file_format
    alias: file_format
    owner: AnnotationSemanticSegmentationMaskFile
    domain_of:
    - AnnotationSourceFile
    - AnnotationOrientedPointFile
    - AnnotationInstanceSegmentationFile
    - AnnotationPointFile
    - AnnotationSegmentationMaskFile
    - AnnotationSemanticSegmentationMaskFile
    range: string
    inlined: true
    inlined_as_list: true
  glob_string:
    name: glob_string
    from_schema: metadata
    exact_mappings:
    - cdp-common:annotation_source_file_glob_string
    alias: glob_string
    owner: AnnotationSemanticSegmentationMaskFile
    domain_of:
    - AnnotationSourceFile
    - AnnotationOrientedPointFile
    - AnnotationInstanceSegmentationFile
    - AnnotationPointFile
    - AnnotationSegmentationMaskFile
    - AnnotationSemanticSegmentationMaskFile
    range: string
    inlined: true
    inlined_as_list: true
  is_visualization_default:
    name: is_visualization_default
    from_schema: metadata
    exact_mappings:
    - cdp-common:annotation_source_file_is_visualization_default
    alias: is_visualization_default
    owner: AnnotationSemanticSegmentationMaskFile
    domain_of:
    - AnnotationSourceFile
    - AnnotationOrientedPointFile
    - AnnotationInstanceSegmentationFile
    - AnnotationPointFile
    - AnnotationSegmentationMaskFile
    - AnnotationSemanticSegmentationMaskFile
    range: string
    inlined: true
    inlined_as_list: true

```
</details>

### Induced

<details>
```yaml
name: AnnotationSemanticSegmentationMaskFile
description: File and sourcing data for a semantic segmentation mask annotation. Annotation
  that identifies classes of objects.
from_schema: metadata
aliases:
- SemanticSegmentationMask
is_a: AnnotationSourceFile
attributes:
  mask_label:
    name: mask_label
    description: The mask label for a semantic segmentation mask annotation file.
    from_schema: metadata
    exact_mappings:
    - cdp-common:annotation_source_file_mask_label
    rank: 1000
    ifabsent: int(1)
    alias: mask_label
    owner: AnnotationSemanticSegmentationMaskFile
    domain_of:
    - AnnotationSemanticSegmentationMaskFile
    range: integer
    inlined: true
    inlined_as_list: true
  file_format:
    name: file_format
    from_schema: metadata
    exact_mappings:
    - cdp-common:annotation_source_file_format
    alias: file_format
    owner: AnnotationSemanticSegmentationMaskFile
    domain_of:
    - AnnotationSourceFile
    - AnnotationOrientedPointFile
    - AnnotationInstanceSegmentationFile
    - AnnotationPointFile
    - AnnotationSegmentationMaskFile
    - AnnotationSemanticSegmentationMaskFile
    range: string
    inlined: true
    inlined_as_list: true
  glob_string:
    name: glob_string
    from_schema: metadata
    exact_mappings:
    - cdp-common:annotation_source_file_glob_string
    alias: glob_string
    owner: AnnotationSemanticSegmentationMaskFile
    domain_of:
    - AnnotationSourceFile
    - AnnotationOrientedPointFile
    - AnnotationInstanceSegmentationFile
    - AnnotationPointFile
    - AnnotationSegmentationMaskFile
    - AnnotationSemanticSegmentationMaskFile
    range: string
    inlined: true
    inlined_as_list: true
  is_visualization_default:
    name: is_visualization_default
    from_schema: metadata
    exact_mappings:
    - cdp-common:annotation_source_file_is_visualization_default
    alias: is_visualization_default
    owner: AnnotationSemanticSegmentationMaskFile
    domain_of:
    - AnnotationSourceFile
    - AnnotationOrientedPointFile
    - AnnotationInstanceSegmentationFile
    - AnnotationPointFile
    - AnnotationSegmentationMaskFile
    - AnnotationSemanticSegmentationMaskFile
    range: string
    inlined: true
    inlined_as_list: true

```
</details>