import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;

import java.io.IOException;

public class WebScraper {

    public static void main(String[] args) throws IOException {
        String url = "https://www.investing.com/news/commodities-news/gold-prices-trim-some-weekly-gains-on-tempered-rate-cut-hopes-3445415";
        CloseableHttpClient httpClient = HttpClients.createDefault();
        HttpGet request = new HttpGet(url);
        HttpResponse response = httpClient.execute(request);
        HttpEntity entity = response.getEntity();

        if (entity != null) {
            Document doc = Jsoup.parse(entity.getContent(), "UTF-8", url);
            Element newsSection = doc.select("#XAU/USD News").first();
            if (newsSection != null) {
                Element firstLink = newsSection.select("a").first();
                if (firstLink != null) {
                    System.out.println("First link under XAU/USD News: " + firstLink.attr("href"));
                } else {
                    System.out.println("No link found.");
                }
            } else {
                System.out.println("XAU/USD News section not found.");
            }
        } else {
            System.out.println("Failed to retrieve the page.");
        }

        httpClient.close();
    }
}
