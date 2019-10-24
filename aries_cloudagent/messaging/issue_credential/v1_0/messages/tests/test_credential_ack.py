from ...message_types import CREDENTIAL_ACK
from ..credential_ack import CredentialAck

from unittest import mock, TestCase


class TestCredentialAck(TestCase):
    """Credential ack tests"""

    def test_init(self):
        """Test initializer"""
        credential_ack = CredentialAck()

    def test_type(self):
        """Test type"""
        credential_ack = CredentialAck()

        assert credential_ack._type == CREDENTIAL_ACK

    @mock.patch(
        "aries_cloudagent.messaging.issue_credential.v1_0.messages."
        "credential_ack.CredentialAckSchema.load"
    )
    def test_deserialize(self, mock_credential_ack_schema_load):
        """
        Test deserialize
        """
        obj = CredentialAck()

        credential_ack = CredentialAck.deserialize(obj)
        mock_credential_ack_schema_load.assert_called_once_with(obj)

        assert credential_ack is mock_credential_ack_schema_load.return_value

    @mock.patch(
        "aries_cloudagent.messaging.issue_credential.v1_0.messages."
        "credential_ack.CredentialAckSchema.dump"
    )
    def test_serialize(self, mock_credential_ack_schema_dump):
        """
        Test serialization.
        """
        obj = CredentialAck()

        credential_ack_dict = obj.serialize()
        mock_credential_ack_schema_dump.assert_called_once_with(obj)

        assert credential_ack_dict is mock_credential_ack_schema_dump.return_value


class TestCredentialAckSchema(TestCase):
    """Test credential cred ack schema"""

    credential_ack = CredentialAck()

    def test_make_model(self):
        """Test making model."""
        data = self.credential_ack.serialize()
        model_instance = CredentialAck.deserialize(data)
        assert isinstance(model_instance, CredentialAck)
