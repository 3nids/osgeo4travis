/****************************************************************************
**
** Copyright (C) 2012 Intel Corporation
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtCore module of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL21$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see http://www.qt.io/terms-conditions. For further
** information use the contact form at http://www.qt.io/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 2.1 or version 3 as published by the Free
** Software Foundation and appearing in the file LICENSE.LGPLv21 and
** LICENSE.LGPLv3 included in the packaging of this file. Please review the
** following information to ensure the GNU Lesser General Public License
** requirements will be met: https://www.gnu.org/licenses/lgpl.html and
** http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
**
** As a special exception, The Qt Company gives you certain additional
** rights. These rights are described in The Qt Company LGPL Exception
** version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
**
** $QT_END_LICENSE$
**
****************************************************************************/

#ifndef QIPADDRESS_P_H
#define QIPADDRESS_P_H

//
//  W A R N I N G
//  -------------
//
// This file is not part of the Qt API. It exists for the convenience of
// qurl*.cpp This header file may change from version to version without
// notice, or even be removed.
//
// We mean it.
//

#include "qstring.h"

QT_BEGIN_NAMESPACE

namespace QIPAddressUtils {

typedef quint32 IPv4Address;
typedef quint8 IPv6Address[16];

Q_CORE_EXPORT bool parseIp4(IPv4Address &address, const QChar *begin, const QChar *end);
Q_CORE_EXPORT const QChar *parseIp6(IPv6Address &address, const QChar *begin, const QChar *end);
Q_CORE_EXPORT void toString(QString &appendTo, IPv4Address address);
Q_CORE_EXPORT void toString(QString &appendTo, IPv6Address address);

} // namespace

QT_END_NAMESPACE

#endif // QIPADDRESS_P_H
