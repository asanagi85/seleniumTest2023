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
        self.bondCode = bondCode #채권코드
        self.unitPrice = unitPrice # 채권단가
        self.couponRate = couponRate #표면이율
        self.salesUnit = salesUnit #구매단위
        self.interstPaymentDate = interstPaymentDate #이자지급월
        self.remainingYears = remainingYears #잔존기간
        self.redemptionDate = redemptionDate #만기일
        self.creditRating = creditRating #신용등급
