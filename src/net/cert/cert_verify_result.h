// Copyright (c) 2011 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef NET_CERT_CERT_VERIFY_RESULT_H_
#define NET_CERT_CERT_VERIFY_RESULT_H_

#include <vector>

#include "base/memory/ref_counted.h"
#include "net/base/net_export.h"
#include "net/cert/cert_status_flags.h"
#include "net/cert/ocsp_verify_result.h"
#include "net/cert/x509_cert_types.h"

namespace net {

class X509Certificate;

// The result of certificate verification.
class NET_EXPORT CertVerifyResult {
 public:
  CertVerifyResult();
  CertVerifyResult(const CertVerifyResult& other);
  ~CertVerifyResult();

  void Reset();

  bool operator==(const CertVerifyResult& other) const;

  // The certificate chain that was constructed during verification.
  //
  // Note: Although |verified_cert| will match the originally supplied
  // certificate to be validated, the results of GetIntermediateCertificates()
  // may be substantially different, both in order and in content, then the
  // originally supplied intermediates.
  //
  // In the event of validation failures, this may contain the originally
  // supplied certificate chain or a partially constructed path, depending on
  // the implementation.
  //
  // In the event of validation success, the trust anchor will be
  // |verified_cert->GetIntermediateCertificates().back()| if
  // there was a certificate chain to the trust anchor, and will
  // be |verified_cert->os_cert_handle()| if the certificate was
  // the trust anchor.
  scoped_refptr<X509Certificate> verified_cert;

  // Bitmask of CERT_STATUS_* from net/cert/cert_status_flags.h. Note that
  // these status flags apply to the certificate chain returned in
  // |verified_cert|, rather than the originally supplied certificate
  // chain.
  CertStatus cert_status;

  // Hash algorithms used by the certificate chain, excluding the trust
  // anchor.
  bool has_md2;
  bool has_md4;
  bool has_md5;
  bool has_sha1;
  bool has_sha1_leaf;

  // If the certificate was successfully verified then this contains the
  // hashes for all of the SubjectPublicKeyInfos of the chain (target,
  // intermediates, and trust anchor)
  //
  // The ordering of the hashes in this vector is unspecified. Both the SHA1
  // and SHA256 hash will be present for each certificate.
  HashValueVector public_key_hashes;

  // is_issued_by_known_root is true if we recognise the root CA as a standard
  // root.  If it isn't then it's probably the case that this certificate was
  // generated by a MITM proxy whose root has been installed locally. This is
  // meaningless if the certificate was not trusted.
  bool is_issued_by_known_root;

  // is_issued_by_additional_trust_anchor is true if the root CA used for this
  // verification came from the list of additional trust anchors.
  bool is_issued_by_additional_trust_anchor;

  // True if a fallback to the common name was used when matching the host
  // name, rather than using the subjectAltName.
  bool common_name_fallback_used;

  // Verification of stapled OCSP response, if present.
  OCSPVerifyResult ocsp_result;
};

}  // namespace net

#endif  // NET_CERT_CERT_VERIFY_RESULT_H_
