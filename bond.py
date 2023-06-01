#채권객체
class Bond:
    def __init__(self, bondCode='', unitPrice='',
                 couponRate='',salesUnit = '',
                 interstPaymentDate='',remainingYears='',
                 redemptionDate='',creditRating=''):
        self.bondCode = bondCode
