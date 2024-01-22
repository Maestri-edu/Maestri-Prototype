import { StyleSheet } from "react-native";
import colors from "../../../../design-System/global-styles";

const styles = StyleSheet.create({
    boxCarousel: {
        width: "100%",
        height: "95%",
        backgroundColor: colors.softWhite,
        marginTop: "5%",
        padding: 10
    },
    itemCrousel: {
        width: "100%",
    },
    text: {
        color: colors.mediumGray,
        fontSize: 20,
        fontWeight: "400",
    },

    imageCarouselItem: {
        width: "95%",
        height: "55%",
        marginLeft:"2.5%",
        marginTop:"5%",
        borderRadius:20,
    }
})

export default styles