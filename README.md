# 📖 recitation-all (Version 1.0)

[![jsDelivr](https://data.jsdelivr.com/v1/package/gh/zaibihsn/recitation-all/badge)](https://www.jsdelivr.com/package/gh/zaibihsn/recitation-all)
[![GitHub license](https://img.shields.io/github/license/zaibihsn/recitation-all)](https://github.com/zaibihsn/recitation-all/blob/main/LICENSE)

A comprehensive repository of Quranic recitations, optimized for web and mobile applications. This project provides high-quality audio files in `.opus` format and precise word-by-word timestamp data in `.json` format for 22 world-renowned reciters.

## 🌟 Key Features

- **22 Renowned Reciters**: A wide selection of beautiful recitations.
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
Replace `{reciter-name}` and `{verse-index}` with the actual values.
```
https://cdn.jsdelivr.net/gh/zaibihsn/recitation-all/audio/{reciter-name}/{surah-index}/{verse-index}.opus
```

### Timestamp JSON URL Pattern
```
https://cdn.jsdelivr.net/gh/zaibihsn/recitation-all/data/{reciter-name}/{surah-index}/{verse-index}.json
```

*Note: For reciters using global indexing, the path might be simplified to `{reciter-name}/{verse-global-index}.opus`.*

---

## 🎙️ List of Reciters and Statistics

This repository contains **22 reciters**. Below is the detailed breakdown of files available for each:

| Reciter Name | Audio Files (.opus) | Timestamp Files (.json) |
| :--- | :---: | :---: |
| [Abdul Basit Abdul Samad (Murattal)](https://github.com/zaibihsn/recitation-all/tree/main/abdul-basit-abdul-samad-murattal-hafs-950) | 6236 | 6236 |
| [Abdul Basit Abdul Samad (Mujawwad)](https://github.com/zaibihsn/recitation-all/tree/main/abdul-basit-abdul-samad-mujawwad-hafs-949) | 6236 | 6236 |
| [Abdul Rahman Al-Sudais (Murattal)](https://github.com/zaibihsn/recitation-all/tree/main/abdul-rahman-al-sudais-murattal-hafs-951) | 6236 | 6236 |
| [Abdullah Hamad Abu Sharida](https://github.com/zaibihsn/recitation-all/tree/main/abdullah-hamad-abu-sharida) | 6236 | 6236 |
| [Abdur Rahman As-Sudais (Recitation)](https://github.com/zaibihsn/recitation-all/tree/main/abdur-rahman-as-sudais-recitation) | 6236 | 6236 |
| [Abu Bakr Al-Shatri](https://github.com/zaibihsn/recitation-all/tree/main/abu-bakr-al-shatri-murattal-hafs-952) | 6236 | 6236 |
| [Ahmed Ibn Ali Al-Ajmy](https://github.com/zaibihsn/recitation-all/tree/main/ahmed-ibn-ali-al-ajmy) | 6236 | 6236 |
| [Al-Nufais](https://github.com/zaibihsn/recitation-all/tree/main/alnufais) | 6236 | 6236 |
| [Bandar Baleela](https://github.com/zaibihsn/recitation-all/tree/main/bandar-baleela) | 6236 | 6236 |
| [Hani Ar-Rifai](https://github.com/zaibihsn/recitation-all/tree/main/hani-ar-rifai-recitation-murattal-hafs-68) | 6236 | 6236 |
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

## 🛠️ Technical Details

1. **Audio Format**: Opus (`.opus`) - Optimized for streaming and low-bandwidth scenarios while maintaining high fidelity.
2. **Metadata**: Each verse has a JSON file containing:
   - `reciter_name`
   - `surah`
   - `verse`
   - `audio_url` (reference)
   - `words`: Detailed word-by-word timing (start and end times in milliseconds).
3. **Global Search Index**: The repository supports a 1-6236 indexing system, allowing developers to map verses directly without complex Surah/Ayah logic.

## 📜 License

- **Code License**: This project's infrastructure and scripts are licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
- **Data License & Disclaimer**: For information regarding audio ownership, usage rights, and attributions, please refer to the [DATA_LICENSE.md](DATA_LICENSE.md) file.

---
*Created and maintained by [zaibihsn](https://github.com/zaibihsn).*
