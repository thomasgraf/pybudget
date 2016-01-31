from colander import MappingSchema
from colander import SchemaNode
from colander import String
from colander import Integer
from colander import Decimal
from colander import Date
from colander import deferred
import deform


class ExpenseSchema(MappingSchema):
    """Schema for adding and editing expenses to the database."""
    account = SchemaNode(
        colander.String(),
        widget=deform.widget.SelectWidget(
        values=(
            ('', '-- Wählen --'),
            ('bar', 'Bar'),
            ('ec', 'EC-Karte'),
            ('visa', 'VISA'),
            ('mastercard','MAstercard')
        ))
    )
    expense_date = SchemaNode(
        Date(),
    )
    amount = SchemaNode(
        Decimal(),
        widget = deform.widget.MoneyInputWidget(
            size=20,
            options={'allowZero':True}
        )
    )

    category = SchemaNode(
        colander.String(),
        widget=deform.widget.SelectWidget(
        values=(
            ('', '-- Wählen --'),
            ('lebensmittel', 'Lebensmittel'),
            ('hyg_haus', 'Hygiene/Haushalt'),
            ('kleidung', 'Kleidung'),
            ('sonstiges','Sonstiges')
        ))
    )