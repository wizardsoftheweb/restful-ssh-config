"""This file provides the Keyword model"""
# pylint: disable=too-few-public-methods


from restful_ssh_config import DATABASE
from restful_ssh_config.models import HOST_CONFIG_LOOKUP, KEYWORD_HOST_LOOKUP

# pylint: disable=invalid-name
# pylint: disable=no-member
Column = DATABASE.Column
SqlString = DATABASE.String
# pylint: enable=no-member
# pylint: enable=invalid-name


class Host(DATABASE.Model):
    """This class sets up the fields for the Keyword model"""

    __tablename__ = 'hosts'

    reference_name = Column(
        SqlString(255),
    )
    config_files = DATABASE.relationship(  # pylint: disable=no-member
        'ConfigFile',
        secondary=HOST_CONFIG_LOOKUP,
        lazy='subquery',
    )
    keywords = DATABASE.relationship(  # pylint: disable=no-member
        'Keyword',
        secondary=KEYWORD_HOST_LOOKUP,
        lazy='subquery',
        backref=DATABASE.backref(  # pylint: disable=no-member
            'hosts',
            lazy=True,
        ),
    )

    def __repr__(self):
        return "<Host %d - %r>" % (self.id, self.reference_name)
