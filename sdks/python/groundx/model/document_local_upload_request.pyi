# coding: utf-8

"""
    GroundX API

    Ground Your RAG Apps in Fact not Fiction

    The version of the OpenAPI document: 1.0.0
    Contact: support@groundx.ai
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from groundx import schemas  # noqa: F401


class DocumentLocalUploadRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def blob() -> typing.Type['DocumentLocalUploadRequestBlob']:
                return DocumentLocalUploadRequestBlob
            bucketId = schemas.IntSchema
            fileName = schemas.StrSchema
        
            @staticmethod
            def fileType() -> typing.Type['DocumentType']:
                return DocumentType
            metadata = schemas.DictSchema
            callbackData = schemas.StrSchema
            callbackUrl = schemas.StrSchema
            __annotations__ = {
                "blob": blob,
                "bucketId": bucketId,
                "fileName": fileName,
                "fileType": fileType,
                "metadata": metadata,
                "callbackData": callbackData,
                "callbackUrl": callbackUrl,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blob"]) -> 'DocumentLocalUploadRequestBlob': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bucketId"]) -> MetaOapg.properties.bucketId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileName"]) -> MetaOapg.properties.fileName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileType"]) -> 'DocumentType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callbackData"]) -> MetaOapg.properties.callbackData: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callbackUrl"]) -> MetaOapg.properties.callbackUrl: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["blob", "bucketId", "fileName", "fileType", "metadata", "callbackData", "callbackUrl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blob"]) -> typing.Union['DocumentLocalUploadRequestBlob', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bucketId"]) -> typing.Union[MetaOapg.properties.bucketId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileName"]) -> typing.Union[MetaOapg.properties.fileName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileType"]) -> typing.Union['DocumentType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callbackData"]) -> typing.Union[MetaOapg.properties.callbackData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callbackUrl"]) -> typing.Union[MetaOapg.properties.callbackUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["blob", "bucketId", "fileName", "fileType", "metadata", "callbackData", "callbackUrl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        blob: typing.Union['DocumentLocalUploadRequestBlob', schemas.Unset] = schemas.unset,
        bucketId: typing.Union[MetaOapg.properties.bucketId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        fileName: typing.Union[MetaOapg.properties.fileName, str, schemas.Unset] = schemas.unset,
        fileType: typing.Union['DocumentType', schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        callbackData: typing.Union[MetaOapg.properties.callbackData, str, schemas.Unset] = schemas.unset,
        callbackUrl: typing.Union[MetaOapg.properties.callbackUrl, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentLocalUploadRequest':
        return super().__new__(
            cls,
            *args,
            blob=blob,
            bucketId=bucketId,
            fileName=fileName,
            fileType=fileType,
            metadata=metadata,
            callbackData=callbackData,
            callbackUrl=callbackUrl,
            _configuration=_configuration,
            **kwargs,
        )

from groundx.model.document_local_upload_request_blob import DocumentLocalUploadRequestBlob
from groundx.model.document_type import DocumentType