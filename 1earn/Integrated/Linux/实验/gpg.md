# gpg

---

## 建立新的 GPG 密钥对

```bash
gpg --gen-key
```

## 导出公钥

```bash
gpg --export {user-name}
gpg --export ffffffff0x > ffffffff0x-pub.gpg
```

## 导入其他人的公钥

```bash
gpg --import FileName
```

## 读取加密的消息

```bash
gpg --decrypt test-file.asc
```

---

## Source & Reference
- [Gpg Key-Pair Encryption and Decryption Examples](https://linux.101hacks.com/unix/gpg-command-examples/)
