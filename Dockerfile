FROM python:3
ADD ResourceCreationScript.py /
RUN pip install requests
CMD ["python", "./ResourceCreationScript.py"]
