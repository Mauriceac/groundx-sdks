/* tslint:disable */
/* eslint-disable */
/**
 * GroundX API
 * Ground Your RAG Apps in Fact not Fiction
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@groundx.ai
 *
 * NOTE: This file is auto generated by Konfig (https://konfigthis.com).
 * Do not edit the class manually.
 */

// May contain unused imports in some cases
// @ts-ignore
import { DocumentType } from './document-type';

/**
 * 
 * @export
 * @interface DocumentLocalUploadRequestMetadata
 */
export interface DocumentLocalUploadRequestMetadata {
    /**
     * 
     * @type {number}
     * @memberof DocumentLocalUploadRequestMetadata
     */
    'bucketId'?: number;
    /**
     * 
     * @type {string}
     * @memberof DocumentLocalUploadRequestMetadata
     */
    'fileName'?: string;
    /**
     * 
     * @type {DocumentType}
     * @memberof DocumentLocalUploadRequestMetadata
     */
    'fileType'?: DocumentType;
    /**
     * 
     * @type {object}
     * @memberof DocumentLocalUploadRequestMetadata
     */
    'metadata'?: object;
    /**
     * 
     * @type {string}
     * @memberof DocumentLocalUploadRequestMetadata
     */
    'callbackData'?: string;
    /**
     * 
     * @type {string}
     * @memberof DocumentLocalUploadRequestMetadata
     */
    'callbackUrl'?: string;
}
