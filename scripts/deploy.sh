#!/bin/bash
set -e

datasette publish vercel tg_observer.db \
	--template-dir=templates \
	--static=static:static \
	--metadata metadata.yml \
	--project tg-observer \
	--install=datasette-template-sql
