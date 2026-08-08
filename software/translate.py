"""
translate.py — KrishiMitra AI
Maps English disease class names to farmer-facing Hindi names.
"""

DISEASE_TRANSLATIONS = {
    "Potato___Early_blight": "आलू - अगेती झुलसा रोग",
    "Potato___Late_blight": "आलू - पछेती झुलसा रोग",
    "Potato___healthy": "आलू - स्वस्थ पत्ता",
    "Rice_Bacterial_Leaf_Blight": "धान - जीवाणु पत्ती झुलसा रोग",
    "Rice_Brown_Spot": "धान - भूरा धब्बा रोग",
    "Rice_Healthy_Rice_Leaf": "धान - स्वस्थ पत्ता",
    "Rice_Leaf_Blast": "धान - पत्ती झोंका रोग",
    "Rice_Leaf_scald": "धान - पत्ती अंगमारी रोग",
    "Rice_Sheath_Blight": "धान - आवरण झुलसा रोग",
    "Tomato_Bacterial_spot": "टमाटर - जीवाणु धब्बा रोग",
    "Tomato_Early_blight": "टमाटर - अगेती झुलसा रोग",
    "Tomato_Late_blight": "टमाटर - पछेती झुलसा रोग",
    "Tomato_Leaf_Mold": "टमाटर - पत्ती फफूंद रोग",
    "Tomato_Septoria_leaf_spot": "टमाटर - सेप्टोरिया पत्ती धब्बा रोग",
    "Tomato_Spider_mites_Two_spotted_spider_mite": "टमाटर - मकड़ी कीट प्रकोप",
    "Tomato__Target_Spot": "टमाटर - लक्ष्य धब्बा रोग",
    "Tomato__Tomato_YellowLeaf__Curl_Virus": "टमाटर - पीत पत्ती मोड़क विषाणु रोग",
    "Tomato__Tomato_mosaic_virus": "टमाटर - मोज़ेक विषाणु रोग",
    "Tomato_healthy": "टमाटर - स्वस्थ पत्ता",
    "Wheat_Black_Rust": "गेहूं - काला रतुआ रोग",
    "Wheat_Brown_Rust": "गेहूं - भूरा रतुआ रोग",
    "Wheat_Healthy": "गेहूं - स्वस्थ पत्ता",
    "Wheat_Leaf_Blight": "गेहूं - पत्ती झुलसा रोग",
    "Wheat_Mildew": "गेहूं - चूर्णिल फफूंद रोग",
    "Wheat_Septoria": "गेहूं - सेप्टोरिया रोग",
    "Wheat_Smut": "गेहूं - कंडुआ रोग",
    "Wheat_Tan_spot": "गेहूं - टैन धब्बा रोग",
    "Wheat_Yellow_Rust": "गेहूं - पीला रतुआ रोग",
}


def translate_disease(english_name):
    """Returns the Hindi name for a disease class, or the original name if not found."""
    return DISEASE_TRANSLATIONS.get(english_name, english_name)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python translate.py <english_class_name>")
        sys.exit(1)
    print(translate_disease(sys.argv[1]))
