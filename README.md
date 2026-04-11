# 📖 recitation-all (Version 1.0)

[![jsDelivr](https://data.jsdelivr.com/v1/package/gh/zaibihsn/recitation-all/badge)](https://www.jsdelivr.com/package/gh/zaibihsn/recitation-all)
[![GitHub license](https://img.shields.io/github/license/zaibihsn/recitation-all)](https://github.com/zaibihsn/recitation-all/blob/main/LICENSE)

A comprehensive repository of Quranic recitations, optimized for web and mobile applications. This project provides high-quality audio files in `.opus` format and precise word-by-word timestamp data in `.json` format for 23 world-renowned reciters.

## 🌟 Key Features

- **23 Renowned Reciters**: A wide selection of beautiful recitations.
- **Optimized for Web**: All audio files are converted to `.opus` format for superior compression and quality.
- **Precise Timestamps**: Every verse includes a corresponding JSON file with word-by-word timing data.
- **Global Indexing**: Files are organized using a global search index (1 to 6236), covering every verse of the Quran.
- **CDN Ready**: Easily accessible via jsDelivr for fast integration.

## 📚 Data Source Credits

The recitations and timing data in this repository were meticulously gathered and processed from the following trusted sources:
- [Qul (Tarteel.ai)](https://qul.tarteel.ai/)
- [Quranicaudio.com](https://quranicaudio.com/)
- [Quran.com](https://quran.com/)

---

## ⚡ How to Use as CDN (jsDelivr)

You can use this repository as a high-speed CDN for your frontend applications.

### Audio URL Pattern
Replace `{reciter-name}`, `{surah-index}`, and `{verse-index}` with the corresponding values (surah and verse must be 3-digit zero-padded).
```text
https://cdn.jsdelivr.net/gh/zaibihsn/recitation-all@main/{reciter-name}/{surah-index}/{surah-index}{verse-index}.opus
```

### Timestamp JSON URL Pattern
```text
https://cdn.jsdelivr.net/gh/zaibihsn/recitation-all@main/{reciter-name}/{surah-index}/{surah-index}{verse-index}.json
```

---

## 🎙️ List of Reciters and Statistics

This repository contains **23 reciters**. Below is the detailed breakdown of files available for each:

| Reciter Name | Audio Files (.opus) | Timestamp Files (.json) |
| :--- | :---: | :---: |
| [Abdul Basit Abdul Samad (Murattal)](https://github.com/zaibihsn/recitation-all/tree/main/abdul-basit-abdul-samad-murattal-hafs-950) | 6236 | 6236 |
| [Abdul Basit Abdul Samad (Mujawwad)](https://github.com/zaibihsn/recitation-all/tree/main/abdul-basit-abdul-samad-mujawwad-hafs-949) | 6236 | 6236 |
| [Abdul Rahman Al-Sudais (Murattal)](https://github.com/zaibihsn/recitation-all/tree/main/abdul-rahman-al-sudais-murattal-hafs-951) | 6236 | 6236 |
| [Abdullah Hamad Abu Sharida](https://github.com/zaibihsn/recitation-all/tree/main/abdullah-hamad-abu-sharida) | 6236 | 6236 |
| [Abu Bakr Al-Shatri](https://github.com/zaibihsn/recitation-all/tree/main/abu-bakr-al-shatri-murattal-hafs-952) | 6236 | 6236 |
| [Ahmed Ibn Ali Al-Ajmy](https://github.com/zaibihsn/recitation-all/tree/main/ahmed-ibn-ali-al-ajmy) | 6236 | 6236 |
| [Al-Nufais](https://github.com/zaibihsn/recitation-all/tree/main/alnufais) | 6236 | 6236 |
| [Bandar Baleela](https://github.com/zaibihsn/recitation-all/tree/main/bandar-baleela) | 6236 | 6236 |
| [Hady Toure](https://github.com/zaibihsn/recitation-all/tree/main/surah-recitation-hady-toure) | 6236 | 6236 |
| [Hani Ar-Rifai](https://github.com/zaibihsn/recitation-all/tree/main/hani-ar-rifai-recitation-murattal-hafs-68) | 6236 | 6236 |
| [Khalid Al-Jalil](https://github.com/zaibihsn/recitation-all/tree/main/khalid-al-jalil-murattal-hafs) | 6236 | 6236 |
| [Khalifa Al-Tunaiji](https://github.com/zaibihsn/recitation-all/tree/main/khalifa-al-tunaiji-murattal-hafs-958) | 6236 | 6236 |
| [Maher Al-Muaiqly](https://github.com/zaibihsn/recitation-all/tree/main/maher-al-mu-aiqly-murattal-hafs-948) | 6236 | 6236 |
| [Mahmoud Khalil Al-Husary (Mujawwad)](https://github.com/zaibihsn/recitation-all/tree/main/mahmoud-khalil-al-husary-mujawwad-hafs-956) | 6236 | 6236 |
| [Mahmoud Khalil Al-Husary (Murattal)](https://github.com/zaibihsn/recitation-all/tree/main/mahmoud-khalil-al-husary-murattal-hafs-955) | 6236 | 6236 |
| [Mahmoud Khalil Al-Husary (Alternate)](https://github.com/zaibihsn/recitation-all/tree/main/mahmoud-khalil-al-husary-murattal-hafs-957) | 6236 | 6236 |
| [Minshawi Kids Repeat](https://github.com/zaibihsn/recitation-all/tree/main/minshawi-kids-repeat) | 6184 | 6185 |
| [Mishari Rashid Al-Afasy](https://github.com/zaibihsn/recitation-all/tree/main/mishari-rashid-al-afasy-murattal-hafs-953) | 6236 | 6236 |
| [Mohamed Al-Tablawi](https://github.com/zaibihsn/recitation-all/tree/main/mohamed-al-tablawi-recitation-murattal-hafs-73) | 6236 | 6236 |
| [Muhammad Siddiq Al-Minshawi](https://github.com/zaibihsn/recitation-all/tree/main/muhammad-siddiq-al-minshawi-murattal-hafs-959) | 6236 | 6236 |
| [Saad Al-Ghamdi](https://github.com/zaibihsn/recitation-all/tree/main/saad-al-ghamdi-murattal-hafs-954) | 6236 | 6236 |
| [Saud Al-Shuraim](https://github.com/zaibihsn/recitation-all/tree/main/saud-al-shuraim-murattal-hafs-960) | 6236 | 6236 |
| [Yasser Al-Dosari](https://github.com/zaibihsn/recitation-all/tree/main/yasser-al-dosari-murattal-hafs-961) | 6236 | 6236 |

---

## 🛠️ Technical Details & Implementation

1. **Audio Format**: Opus (`.opus`) - Optimized for streaming and low-bandwidth scenarios while maintaining high fidelity.
2. **Metadata Formats**: Each verse has a `.json` file containing word-by-word timestamps. The JSON structure will be either a flat array or a detailed segment object depending on the original data source.
3. **Directory Structure**: Audio and JSON files are structured inside their respective reciter directory using their 3-digit zero-padded Surah/Verse logic (e.g., `/{reciter_name}/{surah_index}/{surah_index}{verse_index}.opus`).

**📖 Implementation Guide**
Please refer to our comprehensive [**IMPLEMENTATION.md**](IMPLEMENTATION.md) for detailed descriptions of the JSON formats, code examples in **React, Vue, Flutter, and Vanilla JS**, and a ready-to-use **AI Prompt** to help you generate your app's code instantly.

## 📜 License

- **Code License**: This project's infrastructure and scripts are licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
- **Data License & Disclaimer**: For information regarding audio ownership, usage rights, and attributions, please refer to the [DATA_LICENSE.md](DATA_LICENSE.md) file.

---
*Created and maintained by [zaibihsn](https://github.com/zaibihsn).*
