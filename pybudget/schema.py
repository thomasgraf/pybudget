from colander import MappingSchema
from colander import SchemaNode
from colander import String
from colander import Integer
from colander import DateTime
from colander import deferred

class ExpenseSchema(MappingSchema):
    """Schema for adding and editing expenses to the database."""
    name = SchemaNode(String())
    tags = SchemaNode(
        String(),
        widget=TagsWidget(
            autocomplete_url='/tags.autocomplete',
        ),
        description=(
            "Enter a comma after each tag to add it. Backspace to delete."
        ),
        missing=[],
    )
    due_date = SchemaNode(
        deferred_datetime_node,
        missing=None,
    )