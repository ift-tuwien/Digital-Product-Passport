# Digital Product Passport (DPP)

- It follows a defined data schema, supports tiered access for different users, and registers with the EU's central DPP registry {cite:p}`passportcraft2026example`.
- Data that should be part of DPP {cite:p}`gleich2024asset`:
  - General Data
  - Bill of Materials
  - Manufacturing & Transport
  - Design: repair and disassembly instructions
  - Life-cycle: product use, maintenance and repair
  - Carbon footprint
- JSON-LD as preferred format {cite:p}`mypp2026format`

# Standard

- List of standards:
  - EN 18216: Digital product passport - Data exchange protocols
  - EN 18219: Digital product passport - Unique identifiers

## EN 18216: Data exchange protocols

- Data protocol:
  - HTTP/2 or later
- Data formats:
  - Required:
    - JSON
    - HTML (for presentation)
  - Optional:
    - XML
    - JSON LD
- Security:
  - TLS
- API:
  - Should be RESTful

## EN 18219: Unique identifiers

- Requirements:
  - No reassignment
  - Distinct
  - Non-coexistence
  - Cross domain identification
- Persistence:
  - Consistency
  - Preservation
  - Permanence
- Syntax:
  - Use ISO/IEC 646:1991 (ASCII) encoding
  - Either use URL for identification or allow conversion to URL
- Openness:
  - Transparency: fair, reasonable, and non-discriminatory (FRAND)
  - Consumer usage: No special software for users required
  - No undue restrictions: No vendor-lock-in
- ID Schema:
  - Use [ISO/IEC 15459](https://esprregistry.com/iso-15459-data-carriers/): e.g. GS1 GTIN (ISO/IEC 15459 compatible) for model and serial number to identify specific product

## QR Code

- GS1 Digital Link for QR codes
  - Specification for:
    - [URIs](https://ref.gs1.org/standards/digital-link/uri-syntax/)
    - [Compression of URIs](https://ref.gs1.org/standards/digital-link/compression/)
    - [Resolver](https://ref.gs1.org/standards/resolver/)
- Digital Product Passport API: https://dpp.basyx.org

## Apps

### tappr

- [Homepage](https://www.usetappr.com)
- Drag & Drop Passport builder
