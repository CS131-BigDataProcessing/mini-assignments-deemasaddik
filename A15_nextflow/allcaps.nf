#!/usr/bin/env nextflow

// Define the pipeline
params.str = 'Hello World'

process convertToCaps {
    input:
    val inputString from params.str

    output:
    path 'output.txt'

    script:
    """
    echo "$inputString" | tr '[:lower:]' '[:upper:]' > output.txt
    """
}

workflow {
    convertToCaps()
}

