import { Image, Text, View } from "react-native";
import Swiper from "react-native-swiper";
import card1Image from "../../../../../../assets/Venha_fazer_um_ensino_de_qualidade_na_Maestri.edu.jpg"
import card2Image from "../../../../../../assets/ensino_medio_de_qualidade_Maestri.edu.png"
import card3Image from "../../../../../../assets/estude_conosco_Maestri.edu.png"
import styles from "./styles";

const CarouselResources = () => {
    return (
        <View style={styles.boxCarousel}>
            <Text style={styles.text}> para você </Text>
            <Swiper>
                <View style={styles.itemCrousel}>
                    <Image style={styles.imageCarouselItem} source={card1Image} />
                </View>
                <View style={styles.itemCrousel}>
                    <Image style={styles.imageCarouselItem} source={card2Image} />
                </View>
                <View style={styles.itemCrousel}>
                    <Image style={styles.imageCarouselItem} source={card3Image} />
                </View>
            </Swiper>
        </View>
    )
}

export default CarouselResources;
