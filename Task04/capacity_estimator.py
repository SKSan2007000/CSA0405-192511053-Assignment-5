#!/usr/bin/env python3
import argparse, math
p=argparse.ArgumentParser()
p.add_argument("--students",type=int,default=150000)
p.add_argument("--window-hours",type=float,default=2)
p.add_argument("--peak-factor",type=float,default=10)
p.add_argument("--measured-rps",type=float,default=3367.16)
p.add_argument("--utilisation",type=float,default=.70)
a=p.parse_args()
avg=a.students/(a.window_hours*3600)
peak=avg*a.peak_factor
safe=a.measured_rps*a.utilisation
instances=math.ceil(peak/safe)
print(f"Students: {a.students}")
print(f"Average arrival rate: {avg:.2f} logins/s")
print(f"Peak design rate ({a.peak_factor:g}x): {peak:.2f} logins/s")
print(f"Measured local synthetic endpoint throughput: {a.measured_rps:.2f} req/s")
print(f"Planning capacity at {a.utilisation:.0%} utilisation: {safe:.2f} req/s per instance")
print(f"Arithmetic minimum instances using this synthetic benchmark: {instances}")
print("CAUTION: not a production sizing result; login flows, database, TLS, cache misses and user think-time were not modelled.")
