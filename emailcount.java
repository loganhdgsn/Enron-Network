import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class emailCount{

	public static class TokenizerMapper extends Mapper<Object, Text, Text, IntWritable>{

		private final static IntWritable one = new IntWritable(1);
		private Text word = new Text();

		public void map(Object key, Text value, Context context) throws IOException, InterruptedException{
			StringTokenizer itr = new StringTokenizer(value.toString(),"\n");
			String from = "BLANKF";
			String to = "BLANKT";
			String temp;
			Boolean trying = true;
			while(itr.hasMoreTokens()){
				while (trying){
					try{
						from = itr.nextToken();
						from = from.replaceAll("From:","").replaceAll(" ","");
						trying = false;
					}
					catch (Exception e){
						System.out.println("ex");
					}
				}
				while (trying){
						try{
							to = itr.nextToken();
							to = to.replaceAll("To:","").replaceAll(" ","");
							trying = false;
						}
						catch (Exception e){
							System.out.println("ex");
						}
					}
				if (to.compareToIgnoreCase(from) < 0){
							temp = to + ":" + from;
							word.set(temp);
				}
				else{
					temp = from + ":" + to;
					word.set(temp);
				}
				context.write(word, one);
				word.set(to);
				context.write(word, one);
				word.set(from);
				context.write(word, one);
				trying = true;
					}
				}
			}


	public static class IntSumReducer extends Reducer<Text, IntWritable, Text, IntWritable>{

		private IntWritable result = new IntWritable();

		public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {

			int sum = 0;
			for(IntWritable val : values) {
				sum += val.get();
			}
			result.set(sum);
			context.write(key, result);
		}
	}

	public static void main(String [] args) throws Exception {
		Configuration conf = new Configuration();
		Job job = Job.getInstance(conf, "email count");
		job.setJarByClass(emailCount.class);
		job.setMapperClass(TokenizerMapper.class);
		job.setCombinerClass(IntSumReducer.class);
		job.setReducerClass(IntSumReducer.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
		System.exit(job.waitForCompletion(true) ? 0 : 1);
	}
}
