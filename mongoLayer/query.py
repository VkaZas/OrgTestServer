from mongoLayer.models import Customer, Record
import datetime


def update_customer_prize_record(openid, gender, province, prizeid, timestamp=datetime.datetime.utcnow):
    customer = Customer.objects().get(openid=openid)
    record = Record(prizeid=prizeid, timestamp=timestamp)

    # Customer does not exist, create a new customer
    if not customer:
        customer = Customer(openid=openid, gender=gender, province=province, prizeid=prizeid, timestamp=timestamp)

    customer.records.append(record)
    customer.save()


def update_customer_participation_record(openid, prizeid, timestamp=datetime.datetime.utcnow):
    try:
        customer = Customer.objects().get(openid=openid)
        records = customer.records

        # Find the corresponding prize record and mark as participated
        for record in records:
            if record.priceid == prizeid:
                record.participation = True
                break

        customer.save()
    except Exception as e:
        print('Error occurred in update_customer_participation_record()')
        print(str(e))
