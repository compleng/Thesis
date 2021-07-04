import os
path  = os.getcwd()
filenames = os.listdir(path)
for filename in filenames:
   with open(filename, "r") as f:
       lines = f.readlines()
   with open(filename, "w") as f:
       for line in lines:
           if line.strip("\n") != "[**] [116:6:1] \"(ipv4) IPv4 datagram length > captured length\" [**]":
             if line.strip("\n") != "[**] [134:3:1] \"(latency) packet fastpathed due to latency\" [**]":
                if line.strip("\n") != "[**] [129:8:1] \"(stream_tcp) data sent on stream after TCP reset sent\" [**]":
                   if line.strip("\n") != "[**] [129:18:1] \"(stream_tcp) data sent on stream after TCP reset received\" [**]":
                      if line.strip("\n") != "[**] [116:58:1] \"(tcp) experimental TCP options found\" [**]":
                             f.write(line)
