import twitter4j.Twitter;
import twitter4j.TwitterFactory;
import twitter4j.conf.ConfigurationBuilder;

public class ConfigFile {
	
	private static ConfigurationBuilder configure() {
		
		ConfigurationBuilder cb = new ConfigurationBuilder();
		cb.setDebugEnabled(true).
		
		setOAuthConsumerKey(Secret.cKey).
		setOAuthConsumerSecret(Secret.cSecret).
		setOAuthAccessToken("").
		setOAuthAccessTokenSecret("");
		
		return cb;
		
	}
	
	public static TwitterFactory createFactory() {
		ConfigurationBuilder cb = configure();
		TwitterFactory tf = new TwitterFactory(cb.build());
		return tf;
	}
	
	public static Twitter createTwitterObject() {
		
		TwitterFactory tf = createFactory();
		Twitter twitter = tf.getInstance();
		
		return twitter;
	}

}


