# (C) Copyright 2024 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

from earthkit.data.indexing.fieldlist import FieldArray


def demo_source(context, dates, **kargs):

    fields = []

    # for date in dates:
    #     fields.append(...)

    return FieldArray(fields)
