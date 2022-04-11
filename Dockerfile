FROM python:3.7-alpine as build
WORKDIR /wheels
RUN apk add --no-cache \
    g++ \
    gcc \
    git \
    libxml2 \
    libxml2-dev \
    libxslt-dev \
    linux-headers
COPY requirements.txt /opt/cuthes/
RUN pip3 wheel -r /opt/cuthes/requirements.txt


FROM python:3.7-alpine
WORKDIR /opt/cuthes
ARG VCS_REF
ARG VCS_URL="https://github.com/Enmn/cuthes"
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url=$VCS_URL
COPY --from=build /wheels /wheels
COPY . /opt/cuthes/
RUN pip3 install -r requirements.txt -f /wheels \
  && rm -rf /wheels \
  && rm -rf /root/.cache/pip/*

ENTRYPOINT ["python", "main.py"]