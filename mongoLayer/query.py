from mongoLayer.models import Customer, Record
import datetime


def update_customer_prize_record(openid, gender, province, city, prizeid, qrcode, timestamp=datetime.datetime.utcnow):
    num = Customer.objects().filter(openid=openid).count()
    if num == 1:
        customer = Customer.objects().get(openid=openid)
    elif num == 0:
        # Customer does not exist, create a new customer
        customer = Customer(openid=openid, gender=gender, province=province, city=city)
    else:
        print('Error: Multiple records on openid = ' + str(openid))
        return

    record = Record(prizeid=prizeid, timestamp=timestamp, qrcode=qrcode)

    customer.records.append(record)
    customer.save()


def update_customer_participation_record(openid, prizeid, timestamp=datetime.datetime.utcnow):
    try:
        customer = Customer.objects().get(openid=openid)
        records = customer.records

        # Find the corresponding prize record and mark as participated
        for record in records:
            if record.prizeid == prizeid:
                record.participation = True
                break

        customer.save()
    except Exception as e:
        print('Error occurred in update_customer_participation_record()')
        print(str(e))
