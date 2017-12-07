import java.util.List;
import java.util.ArrayList;

import twitter4j.Query;
import twitter4j.QueryResult;
import twitter4j.ResponseList;
import twitter4j.Status;
import twitter4j.Twitter;
import twitter4j.TwitterException;

public class TwitterCaller {

		public static final Twitter twitter = ConfigFile.createTwitterObject();
		
		public static void main (String[] args) {
			
			
			try {
				ResponseList<Status> statuses = twitter.getUserTimeline("realDonaldTrump");
				printStatuses(statuses);
			} catch (Exception e) {
				System.out.println(e.getMessage());
			}
		}
		
		public static void printStatuses(List<Status> statuses) {
			ArrayList<TwitterProperty> tweets = new ArrayList<TwitterProperty>();
			
			for (Status status : statuses) {
				tweets.add(buildProperty(status));
			}
			for (TwitterProperty t : tweets) {
				System.out.println("Sent: " + t.getSentDate());
				System.out.println("Tweet: " + t.getText());
				System.out.println("");
			}
		}
		
		public static TwitterProperty buildProperty(Status status) {
			TwitterProperty prop = new TwitterProperty();
			
			prop.setSenderID(status.getUser().getId());
			prop.setSenderSN(status.getUser().getScreenName());
			prop.setLocation(status.getGeoLocation());
			prop.setName(status.getUser().getName());
			prop.setSentDate(status.getCreatedAt());
			prop.setText(status.getText());
			prop.setTweetID(status.getId());

			prop.setAmtFriends(status.getUser().getFollowersCount());
			prop.setStat(status);
			
			return prop;		
				
		}
}
