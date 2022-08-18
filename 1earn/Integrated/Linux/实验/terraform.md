# terraform

---

## vultr providers

### vps

- https://registry.terraform.io/providers/vultr/vultr/latest/docs/resources/instance

**main.tf**
```conf
resource "vultr_instance" "f0x" {
    plan = "vc2-2c-4gb"
    region = "sgp"
    os_id = 477
    label = "f0x"
    tags = ["f0x"]
    hostname = "f0x"
    enable_ipv6 = false
    backups = "disabled"
    ddos_protection = false
    activation_email = false
}
```

**outputs.tf**
```conf
output "vps_ip" {
  value       = "${vultr_instance.f0x.main_ip}"
  description = "vps ip."
}
output "vps_os" {
  value       = "${vultr_instance.f0x.os}"
  description = "vps os."
}
output "vps_ram" {
  value       = "${vultr_instance.f0x.ram}"
  description = "vps ram."
}
output "vps_disk" {
  value       = "${vultr_instance.f0x.disk}"
  description = "vps disk."
}
output "vps_allowed_bandwidth" {
  value       = "${vultr_instance.f0x.allowed_bandwidth}"
  description = "vps allowed_bandwidth."
}
output "vps_hostname" {
  value       = "${vultr_instance.f0x.hostname}"
  description = "vps hostname."
}
output "vps_password" {
  value       = nonsensitive(vultr_instance.f0x.default_password)
  description = "vps password."
}
```

**version.tf**
```conf
terraform {
  required_providers {
    vultr = {
      source = "vultr/vultr"
      version = "2.11.3"
    }
  }
}

provider "vultr" {
  # Configuration options
}
```

创建
```
terraform init
terraform apply
```

销毁
```
terraform destroy
```

---

## aliyun providers

### ecs

- https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/auto_provisioning_group

**main.tf**
```conf
resource "alicloud_instance" "instance" {
  security_groups            = alicloud_security_group.group.*.id
  instance_type              = data.alicloud_instance_types.types_ds.instance_types.0.id
  image_id                   = "ubuntu_18_04_64_20G_alibase_20190624.vhd"
  instance_name              = "test_instance"
  vswitch_id                 = alicloud_vswitch.vswitch.id
  system_disk_size           = 20
  internet_max_bandwidth_out = 100

  depends_on = [
    alicloud_security_group.group,
    alicloud_vswitch.vswitch,
  ]
}

resource "alicloud_security_group" "group" {
  name   = "test_security_group"
  vpc_id = alicloud_vpc.vpc.id
  depends_on = [
    alicloud_vpc.vpc
  ]
}

resource "alicloud_security_group_rule" "allow_all_tcp" {
  type              = "ingress"
  ip_protocol       = "tcp"
  nic_type          = "intranet"
  policy            = "accept"
  port_range        = "8080/8080"
  priority          = 1
  security_group_id = alicloud_security_group.group.id
  cidr_ip           = "0.0.0.0/0"
  depends_on = [
    alicloud_security_group.group
  ]
}

resource "alicloud_vpc" "vpc" {
  vpc_name   = "test_vpc"
  cidr_block = "172.16.0.0/16"
}

resource "alicloud_vswitch" "vswitch" {
  vpc_id       = alicloud_vpc.vpc.id
  cidr_block   = "172.16.0.0/24"
  zone_id      = "cn-beijing-h"
  vswitch_name = "test_vswitch"
  depends_on = [
    alicloud_vpc.vpc
  ]
}

resource "alicloud_ram_role" "role" {
  name     = "test-role"
  force    = true
  document = <<EOF
  {
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "ecs.aliyuncs.com"
        ]
      }
    }
  ],
  "Version": "1"
  }
  EOF
}

resource "alicloud_ram_policy" "policy" {
  policy_name     = "AdministratorAccess"
  force           = true
  policy_document = <<EOF
  {
    "Statement": [
        {
            "Action": "*",
            "Effect": "Allow",
            "Resource": "*"
        }
    ],
    "Version": "1"
  }
  EOF
}

resource "alicloud_ram_role_attachment" "attach" {
  role_name    = alicloud_ram_role.role.name
  instance_ids = alicloud_instance.instance.*.id
  depends_on = [
    alicloud_instance.instance
  ]
}

resource "alicloud_ram_role_policy_attachment" "attach" {
  policy_name = alicloud_ram_policy.policy.name
  policy_type = alicloud_ram_policy.policy.type
  role_name   = alicloud_ram_role.role.name
  depends_on = [
    alicloud_ram_policy.policy,
    alicloud_ram_role.role
  ]
}

data "alicloud_instance_types" "types_ds" {
  cpu_core_count = 1
  memory_size    = 1
}
```

**outputs.tf**
```
output "instance_ip" {
  value       = "${alicloud_instance.instance.public_ip}"
  description = "instance_ip."
}
```

**version.tf**
```
terraform {
  required_providers {
    alicloud = {
      source  = "aliyun/alicloud"
      version = "1.171.0"
    }
  }
}

provider "alicloud" {
  profile = "cloud-tool"
  region  = "cn-beijing"
}
```

创建
```
terraform init
terraform apply
```

销毁
```
terraform destroy
```

### eci

- https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/eci_container_group

**main.tf**
```conf
resource "alicloud_eci_container_group" "example" {
  container_group_name = "tf-testacc-eci-gruop"
  cpu                  = 2.0
  memory               = 4.0
  restart_policy       = "OnFailure"
  security_group_id    = alicloud_security_group.group.id
  vswitch_id           = alicloud_vswitch.vswitch.id
  auto_create_eip      = true
  tags = {
    TF = "create"
  }

  containers {
    image             = "registry-vpc.cn-beijing.aliyuncs.com/eci_open/nginx:alpine"
    name              = "nginx"
    working_dir       = "/tmp/nginx"
    image_pull_policy = "IfNotPresent"
    commands          = ["/bin/sh", "-c", "sleep 9999"]
    volume_mounts {
      mount_path = "/tmp/test"
      read_only  = false
      name       = "empty1"
    }
    ports {
      port     = 80
      protocol = "TCP"
    }
    environment_vars {
      key   = "test"
      value = "nginx"
    }
  }

  depends_on = [
    alicloud_security_group.group,
    alicloud_vswitch.vswitch,
  ]
}

resource "alicloud_security_group" "group" {
  name   = "huocorp_terraform_goat_security_group"
  vpc_id = alicloud_vpc.vpc.id
  depends_on = [
    alicloud_vpc.vpc
  ]
}

resource "alicloud_security_group_rule" "allow_all_tcp" {
  type              = "ingress"
  ip_protocol       = "tcp"
  nic_type          = "intranet"
  policy            = "accept"
  port_range        = "80/80"
  priority          = 1
  security_group_id = alicloud_security_group.group.id
  cidr_ip           = "0.0.0.0/0"
  depends_on = [
    alicloud_security_group.group
  ]
}
resource "alicloud_vpc" "vpc" {
  vpc_name   = "huocorp_terraform_goat_vpc"
  cidr_block = "172.16.0.0/16"
}

resource "alicloud_vswitch" "vswitch" {
  vpc_id       = alicloud_vpc.vpc.id
  cidr_block   = "172.16.0.0/24"
  zone_id      = "cn-beijing-h"
  vswitch_name = "huocorp_terraform_goat_vswitch"
  depends_on = [
    alicloud_vpc.vpc
  ]
}
```

**outputs.tf**
```conf
output "eci_container_ip" {
  value       = "${alicloud_eci_container_group.example.internet_ip}"
  description = "eci_container."
}
```

**version.tf**
```conf
terraform {
  required_providers {
    alicloud = {
      source = "aliyun/alicloud"
      version = "1.172.0"
    }
  }
}

provider "alicloud" {
  profile = "cloud-tool"
  region  = "cn-beijing"
}
```

创建
```
terraform init
terraform apply
```

销毁
```
terraform destroy
```

---

## Tips

**随机密码**
```conf
# main.tf

provider "random" {}

resource "random_password" "password" {
  length = 16
  special = true
  override_special = "_%@"
}

resource "aws_db_instance" "example" {
  password = random_password.password.result
}
```

**json 输出**
```
terraform output -json
```

**变量**
- https://lonegunmanb.github.io/introduction-terraform/3.3.%E8%BE%93%E5%85%A5%E5%8F%98%E9%87%8F.html

```conf
variable "test_ip" {
  type        = string
  description = "test server ip"
}

resource "alicloud_instance" "instance" {
  ....
  user_data                  = <<EOF
#!/bin/bash
...
sudo echo "${var.cs_ip}" > /tmp/ip.txt
....
EOF
  .....
}
```

```bash
terraform apply -var="test_ip=1.14.5.14"
```

**插件缓存**

- linux
  ```
  echo 'plugin_cache_dir = "$HOME/.terraform.d/plugin-cache"' > $HOME/.terraformrc
  ```

- windows

  %APPDATA% 目录下 `terraform.rc` 文件
  ```
  plugin_cache_dir = "$HOME/.terraform.d/plugin-cache"
  ```
