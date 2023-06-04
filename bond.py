#채권객체
# class Bond:
    #생성자
    # def __init__(self, bondCode='', unitPrice='',
    #              couponRate='',salesUnit = '',
    #              interstPaymentDate='',remainingYears='',
    #              redemptionDate='',creditRating=''):
    #     self.bondCode = bondCode
    # def setData(self,bondCode,unitPrice,couponRate,salesUnit,interstPaymentDate,
    #             remainingYears,redemptionDate,creditRating):
    #     self.bondCode = bondCode
    #     self.unitPrice = unitPrice
    #     self.couponRate = couponRate
    #     self.salesUnit = salesUnit
    #     self.interstPaymentDate = interstPaymentDate
    #     self.remainingYears = remainingYears
    #     self.redemptionDate = redemptionDate
    #     self.creditRating = creditRating
class Bond:
    def __init__(self, bondCode,unitPrice,couponRate,salesUnit,interstPaymentDate,
                 remainingYears,redemptionDate,creditRating):
        # super(Bond self).__init__(*args))
        self.bondCode = bondCode
        self.unitPrice = unitPrice
        self.couponRate = couponRate
        self.salesUnit = salesUnit
        self.interstPaymentDate = interstPaymentDate
        self.remainingYears = remainingYears
        self.redemptionDate = redemptionDate
        self.creditRating = creditRating
