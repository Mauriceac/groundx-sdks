/*
GroundX API

Ground Your RAG Apps in Fact not Fiction

The version of the OpenAPI document: 1.0.0
Contact: support@groundx.ai

NOTE: This file is auto generated by Konfig (https://konfigthis.com).
*/
import type * as buffer from "buffer"

import { DocumentType } from './document-type';
import { ProcessingStatus } from './processing-status';

/**
 * 
 * @export
 * @interface DocumentResponseDocument
 */
export interface DocumentResponseDocument {
    /**
     * 
     * @type {number}
     * @memberof DocumentResponseDocument
     */
    'bucketId'?: number;
    /**
     * Unique system generated ID for the document
     * @type {string}
     * @memberof DocumentResponseDocument
     */
    'documentId'?: string;
    /**
     * 
     * @type {string}
     * @memberof DocumentResponseDocument
     */
    'fileName'?: string;
    /**
     * The file size of the file stored in GroundX
     * @type {string}
     * @memberof DocumentResponseDocument
     */
    'fileSize'?: string;
    /**
     * The type of document (one of the seven currently supported file types)
     * @type {DocumentType}
     * @memberof DocumentResponseDocument
     */
    'fileType'?: DocumentType;
    /**
     * Unique system generated ID for the ingest request
     * @type {string}
     * @memberof DocumentResponseDocument
     */
    'processId'?: string;
    /**
     * 
     * @type {object}
     * @memberof DocumentResponseDocument
     */
    'searchData'?: object;
    /**
     * Source document URL
     * @type {string}
     * @memberof DocumentResponseDocument
     */
    'sourceUrl'?: string;
    /**
     * 
     * @type {ProcessingStatus}
     * @memberof DocumentResponseDocument
     */
    'status'?: ProcessingStatus;
    /**
     * 
     * @type {string}
     * @memberof DocumentResponseDocument
     */
    'statusMessage'?: string;
}

