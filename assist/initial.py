from assist.models import Stat , Contributor, User, ExamPaper, Material, Announcement, CourseAllotment, Feedback
stats,created =  Stat.objects.get_or_create(tag='initial')
if stats:
	user_count         		= User.objects.filter().count()
	material_count    		= User.objects.filter().count()
	announcement_count		= Announcement.objects.filter().count()
	paper_count        		= ExamPaper.objects.filter().count()
	contributor_count  		= Contributor.objects.filter().count()
	stats.user_count		= user_count
	stats.material_count 	= material_count
	stats.paper_count		= paper_count
	stats.contributor_count = contributor_count
	stats.announcement_count = announcement_count
	stats.save()

users      = User.objects.filter(user_role='student')
if users:
	for user in users:
		contributor,created = Contributor.objects.get_or_create(user=user)
		if contributor:
			contributor.announcement = Announcement.objects.filter(author=user).count()
			contributor.paper        = ExamPaper.objects.filter(author=user).count()
			contributor.material     = Material.objects.filter(author=user).count()
			contributor.feedback     = Feedback.objects.filter(author=user).count()
			contributor.points       = (int(contributor.paper) + int(contributor.announcement) + int(contributor.material))*5 + int(contributor.feedback)*10
			contributor.save()



